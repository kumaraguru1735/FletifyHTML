from bs4 import BeautifulSoup
import flet as ft
from FletifyHTML.html_parser import parse_html_to_flet


def convert_html_to_flet(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    flet_code = parse_html_to_flet(soup)
    return flet_code
