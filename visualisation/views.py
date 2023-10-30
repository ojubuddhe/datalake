from django.shortcuts import render
import csv
from .models import lostdeposit

# Create your views here.
from django.shortcuts import render
from .forms import YourCSVUploadForm

def upload_csv(request):
    if request.method == 'POST':
        form = YourCSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # process the uploaded file (parse CSV and save to database)
            handle_uploaded_file(request.FILES['file'])
            return render(request, 'success.html')
    else:
        form = YourCSVUploadForm()
    return render(request, 'upload.html', {'form': form})




def handle_uploaded_file(f):
    reader = csv.DictReader(f)
    for row in reader:
        lostdeposit.objects.create(
            stateName=row['cstateName'],
            assemblyNumber=row['assemblyNumber'],
            year = row['year'],
            total_Candidates = row['total_Candidates'],
            deposit_Lost = row['deposit_Lost'],
            # Map other columns from the CSV to your model fields
        )


def visualize_data(request):
    data = lostdeposit.objects.all()  # Fetch the data from the database
    context = {'data': data}
    return render(request, 'visualize.html', context)
