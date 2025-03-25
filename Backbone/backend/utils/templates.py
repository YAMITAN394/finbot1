from fastapi.templating import Jinja2Templates
import os

# Get the absolute path to the templates directory
template_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "frontend", "templates")
templates = Jinja2Templates(directory=template_dir)
