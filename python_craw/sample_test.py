from datetime import datetime

print(str(datetime.now()).replace(":", "_").strip().replace(" ", "_").split(".")[0])
