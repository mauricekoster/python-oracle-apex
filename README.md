# python-oracle-apex
Parsing an APEX lang export file into Objects

## Oracle APEX

## APEXLang - reading .apx files

```python
page = parse_apex("examples/login.apx")
```

Better:
```python
parser = ApexParser()
page = parser.parse_file("examples/login.apx")

```

Or from a string:
```python
parser = ApexParser()
content = """page A (
    page: 1000
    name: Hello
    alias: HOME
    title: How the West was won
)
"""
page = parser.parse(content)
assert page.name == "Hello"

```

## Reading yaml files, pre APEX 26.1

```python
page = parse_yaml("examples/login.yaml")
```
