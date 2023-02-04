from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def pdf_convert(request):
    return render(request,'pdf_convert.html')
def pdf_create(request):
    templete_path = "pdf.html"
    context = {"con":"this is context "}
    response = HttpResponse(content_type = 'application/pdf')
    response["Content-Disposition"] = "filename = 'product_report.pdf' "
    template  = get_template(templete_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html,dest=response
    )
    if pisa_status.err:
        return HttpResponse("we had some error")
    return response