import random

import Map
import UI

ui = UI.UI(Map.Map([[random.choice([0, 1]) for i in range(50)] for j in range(50)]))
ui.play()
