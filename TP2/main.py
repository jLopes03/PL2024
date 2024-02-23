import re
import sys

def main():
    html_output = markdown_to_html(sys.stdin.read())
    print(html_output)

def markdown_to_html(markdown_text):

    #converter headers    
    markdown_text = re.sub(r"(#+) (.+)",headers_to_html,markdown_text)
    
    #converter bold
    markdown_text = re.sub(r"\*\*(.+)\*\*",r"<b>\1</b>",markdown_text)

    #converter itálico
    markdown_text = re.sub(r"\*(.+)\*",r"<i>\1</i>",markdown_text)

    #converter imagens
    markdown_text = re.sub(r"!\[(.+)\]\((.+)\)",r'<img src="\2" alt="\1"/>',markdown_text)

    #converter links
    markdown_text = re.sub(r"\[(.+)\]\((.+)\)",r'<a href="\2">\1</a>',markdown_text)
        
    #converter listas numeradas
    html_text = []
    curr_list_number = 0
    for line in markdown_text.splitlines():
        m = re.match(r"(\d+)\. (.+)",line)
        if m:
            html_text.append(f"<ol>\n    <li>{m.group(2)}</li>") if curr_list_number == 0 else html_text.append(f"    <li>{m.group(2)}</li>")
            curr_list_number = m.group(1)

        elif curr_list_number != 0 :
            html_text.append("</ol>")
            html_text.append(line)
            curr_list_number = 0
        
        else:
            html_text.append(line)

    return "\n".join(html_text)


def headers_to_html(matchobj):
    num_hashes = len(matchobj.group(1))
    return f"<h{num_hashes}>{matchobj.group(2)}</h{num_hashes}>"
    
main()