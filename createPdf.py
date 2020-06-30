from jinja2 import FileSystemLoader, Environment, select_autoescape
from weasyprint import HTML, CSS

pdf_context = {}
css_path = ['offer_email.css']
html_file_path = 'addendum_agreement.html'

def create_pdf(html_file_path, pdf_context, css_file_urls):
    BASE_DIR = '/Users/dhruvildave/Development/Cuemath/agreement'
    env = Environment(loader=FileSystemLoader(BASE_DIR), autoescape=select_autoescape(['html', 'xml']))

    template = env.get_template(html_file_path)
    rendered_html = template.render(pdf_context)

    HTML(string=rendered_html).write_pdf(
        stylesheets=[CSS(file_url) for file_url in css_file_urls]
    )

create_pdf(html_file_path, pdf_context, css_path)