#  Copyright (C) 2020. Lizann Brooks
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, version 3 of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>

import re
import requests
from bs4 import BeautifulSoup

print("Getting AO3 website")
website_to_parse = "https://www.archiveofourown.org/works/7863154"
html_doc = requests.get(website_to_parse).text
print("Getting beautiful soup")
soup = BeautifulSoup(html_doc, 'html.parser')

print("Getting download link")
# print(soup.find(class_="download"))
download_links = soup.find(class_="download").find_all("li").children
print(download_links)

# .a.find(href=re.compile("epub"))
