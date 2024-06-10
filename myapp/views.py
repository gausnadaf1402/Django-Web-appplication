from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadCSVForm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import urllib, base64

def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            try:
                df = pd.read_csv(csv_file, on_bad_lines='skip')
            except Exception as e:
                return HttpResponse(f"Error processing CSV file: {e}")
            numeric_df = df.select_dtypes(include=[np.number])
            if numeric_df.empty:
                return HttpResponse("The uploaded CSV file does not contain any numeric data.")

            # Perform data analysis with pandas and numpy
            summary = numeric_df.describe().to_html()

            # Example visualization: correlation heatmap
            plt.figure(figsize=(10, 6))
            correlation = numeric_df.corr()
            sns.heatmap(correlation, annot=True, cmap='coolwarm')
            plt.title('Correlation Heatmap')
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()
            image_base64 = base64.b64encode(image_png).decode('utf-8')

            return render(request, 'analysis/result.html', {
                'summary': summary,
                'image_base64': image_base64,
            })
        else:
            # If form is not valid, re-render the upload page with the form errors
            return render(request, 'analysis/upload.html', {'form': form})
    else:
        form = UploadCSVForm()
        return render(request, 'analysis/upload.html', {'form': form})
