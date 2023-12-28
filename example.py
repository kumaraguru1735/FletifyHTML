from FletifyHTML.converter import convert_html_to_flet
import flet as ft


html_content = """
        <div style="background-color: red;">
            <h1>Title</h1>
            <p style="background-color: red; color:black; font-size:30">This is a paragraph.</p>
            <p style="text-decoration: underline; background-color: blue">This is underlined text.</p>
            <p style="text-decoration: overline;">This has an overline.</p>
            <mark style="background-color:green;">milk vggvgvg</mark>
            <b>This is a bold text</b>
            <strong>This is a STRONG text</strong>
            <p>This is a line.<b>This is a new line</b> la suite.</p>

            <table border="1">
            <tr>
                <th>Header 1</th>
                <th>Header 2</th>
                <th>Header 3</th>
            </tr>
            <tr>
                <td>Row 1, Cell 1</td>
                <td>Row 1, Cell 2</td>
                <td>Row 1, Cell 3</td>
            </tr>
            <tr>
                <td>Row 2, Cell 1</td>
                <td>Row 2, Cell 2</td>
                <td>Row 2, Cell 3</td>
            </tr>
        </table>
            
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
            </ul>
            <a href="https://example.com">Visit Example</a>
            <img src="https://picsum.photos/200/200?10" alt="Example Image">
        </div>
    """
flet_code = convert_html_to_flet(html_content)


def main(page: ft.Page):
    # Example usage:

    page.add(flet_code)
    page.update()


ft.app(target=main)
