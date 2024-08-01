
from django.shortcuts import render

html_cabecera = """
<h1>Mi Portafolio Personal</h1>
<ul>
    <li> <a href="/">Inicio </a> </li>
    <li> <a href="/about-me/">Acerca de </a> </li>
    <li> <a href="/portafolio/">Portafolio </a> </li>
    <li> <a href="/contact/">Contacto </a> </li>
</u>
    """

# Create your views here.
def home (request):
    return render(request, 'core/home.html')


def contact(request):
    return render(request, 'core/contact.html')