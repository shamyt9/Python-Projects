import re

text="My contact is 8978564523"

match=re.search(r'\d{10}',text)
print(re.findall(r"\d+","my age is 20. and I am 70"))

one=re.match(r"\d+","1234hsbc")
two=re.match(r"\d+","hsbc")

print(bool(one))
print(bool(two))

match = re.search(
    r"(?P<year>\d{3})-(?P<month>\d{2})-(?P<day>\d{2})",
    "2026-01-28"
)

print(match.groupdict())