# get-project

```py
import pathlib
from project_tracker.gh import get_project_item_list, get_project_view, is_logged_in, PROJECT_NUMBER
import json


project_number = PROJECT_NUMBER

print(is_logged_in())
#> True

data = get_project_view(project_number)
isinstance(data, dict)
#> True

fpth = pathlib.Path("docs/data/project-view.json")
fpth.write_text(json.dumps(data, indent=4))
fpth.is_file()
#> True
```
