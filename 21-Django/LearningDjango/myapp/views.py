from django.shortcuts import render, HttpResponse

# Create your views here.

layout = """
    <h1>Django web page</h1>
    <hr/>
    <ul>
        <li>
            <a href="/">Home</a>
        </li>
        <li>
            <a href="/hello-world">Hello World</a>
        </li>
        <li>
            <a href="/test-page">Hello World</a>
        </li>
    </ul>
    <hr/>
"""


def index(request):
    html = """
        <h1> Home <h1>
        <p>Years until 2050<p>
        <ul>
    """
    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1
    
    html += "</ul>"

    return HttpResponse(layout+html)

def hello_world(request):
    return HttpResponse(layout+"Hello world with Django!")

def page(request):
    return HttpResponse(layout+"""
        <h1>My web page<h1>
        <h2>Created by Emmanuel Alvarado<h2>
    """)

def contact(request, name=""):
    return HttpResponse(layout+f"""
        <h1>Contact<h1>
        <h2>{name}<h2>
    """)