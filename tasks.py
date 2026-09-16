from invoke import task
from jinja2 import FileSystemLoader, Environment, ChoiceLoader, PackageLoader, TemplateNotFound, TemplateSyntaxError
from pathlib import Path

def get_template(template_name, folder, template_path: Path):
    default_loader = ChoiceLoader(
        [FileSystemLoader(template_path / "templates" / folder)]
    )
    env = Environment(loader=default_loader)
    if not template_name.endswith(".peg") and not template_name.endswith(".sample"):
        template_name += ".peg"
    try:
        template = env.get_template(template_name)
        return template
    except TemplateNotFound:
        print("Template not found")
        return None

    except TemplateSyntaxError:
        print("Template has syntax error")
        return None
    

@task
def build(c, version="26.1"):
    main = get_template("grammar", version, Path.cwd())

    target_peg = Path.cwd() / "src" / "python_oracle_apex" / f"grammar-{version}.peg"
    with target_peg.open("w") as f:
        f.write(main.render())

    print(f"Output written to: {target_peg}")