from bs4 import BeautifulSoup

html_content = """
<html>
    <head>
        <title>Sample HTML Parser</title>
    </head>
    <body>
        <h1>Welcome to my website</h1>
        <p>This is a <em>sample</em> HTML parser.</p>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
    </body>
</html>
"""
soup = BeautifulSoup(html_content, 'html.parser')

tags_to_extract = ["p", "h1", "h2", "h3", "h4", "h5", "h6", "a", "span", "div", "li", "td", "th", "button", "label", "strong", "em", "blockquote", "cite", "code", "pre"]
tag_texts = {}

for tag_name in tags_to_extract:
    tags = soup.find_all(tag_name)
    if tags:
        tag_texts[tag_name] = ' '.join(tag.get_text() for tag in tags)

print(tag_texts)
