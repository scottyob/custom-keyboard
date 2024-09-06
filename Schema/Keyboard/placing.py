
KeyboardLayout = [
  [
    {
      "a": 6
    },
    "Esc",
    "F1",
    "F2",
    "F3",
    "F4",
    "F5",
    "F6",
    "F7",
    "F8",
    "F9",
    "F10",
    "F11",
    "F12",
    {
      "a": 5
    },
    "PrtSc\nNmLk",
    "Pause\nScrLk",
    "Delete\nInsert"
  ],
  [
    {
      "a": 4
    },
    "~\n`",
    "!\n1",
    "@\n2",
    "#\n3",
    "$\n4",
    "%\n5",
    "^\n6",
    "&\n7",
    "*\n8",
    "(\n9",
    ")\n0",
    "_\n-",
    "+\n=",
    {
      "a": 6,
      "w": 2
    },
    "Backspace",
    "Home"
  ],
  [
    {
      "a": 4,
      "w": 1.5
    },
    "Tab",
    "Q",
    "W",
    "E",
    "R",
    "T",
    "Y",
    "U",
    "I",
    "O",
    "P",
    "{\n[",
    "}\n]",
    {
      "w": 1.5
    },
    "|\n\\",
    {
      "a": 6
    },
    "Page Up"
  ],
  [
    {
      "a": 4,
      "w": 1.75
    },
    "Caps Lock",
    "A",
    "S",
    "D",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    ":\n;",
    "\"\n'",
    {
      "a": 6,
      "w": 2.25
    },
    "Enter",
    "Page Down"
  ],
  [
    {
      "w": 2.25
    },
    "Shift",
    {
      "a": 4
    },
    "Z",
    "X",
    "C",
    "V",
    "B",
    "N",
    "M",
    "<\n,",
    ">\n.",
    "?\n/",
    {
      "a": 6,
      "w": 1.75
    },
    "Shift",
    {
      "a": 7
    },
    "↑",
    {
      "a": 6
    },
    "End"
  ],
  [
    "Fn",
    "Ctrl",
    "Option",
    {
      "w": 1.25
    },
    "Cmd",
    {
      "a": 7,
      "w": 6.25
    },
    "",
    {
      "a": 6,
      "w": 1.25
    },
    "Cmd",
    "Option",
    {
      "x": 0.25,
      "a": 7
    },
    "←",
    "↓",
    "→"
  ]
]



KEY_WIDTH = 19.05

switch = 1
y_pos = 0
x_pos = 0
keys = []
next_width = KEY_WIDTH

for row in KeyboardLayout:
	x_pos = 0
	for col in row:
		# If this is a dict, we're going to modify the next key
		# Otherwise, place the key
		if isinstance(col, dict):
			if "w" in col:
				next_width = KEY_WIDTH * col["w"]
			if "x" in col:
				# Just skip through how many X positions to skip
				x_pos += KEY_WIDTH * col["x"]
		else:
			# X position needs to account for width.  If the size is 2,
			# it should be offset by half a KEY_WIDTH
			offset = 0.5 * next_width - 0.5


			# Add the key, and reset the modifier state
			keys.append({
				"id": f"SW{switch}",
				"diode": f"D{switch}",
				"idx": str(switch),
				"x": round(x_pos + offset, 4),
				"y": round(y_pos, 4),
				"width": next_width,
				"key": col,
			})
			switch += 1
			x_pos += next_width
			next_width = KEY_WIDTH

	y_pos += KEY_WIDTH

import pprint
print(pprint.pprint(keys))


# Build a script for the KiCad console to place the layout

cmd = """
import pcbnew

board = pcbnew.GetBoard()
net = board.FindNet("+5V")

"""

for key in keys:
	cmd += 'component = board.FindFootprintByReference("' + key["id"] + '")\n'
	cmd += 'diode = board.FindFootprintByReference("' + key["diode"] + '")\n'
	cmd += 'led = board.FindFootprintByReference("LED' + key["idx"] + '")\n'

	cmd += 'component.SetX(pcbnew.FromMM(' + str(key["x"]) + '))\n'
	cmd += 'component.SetY(pcbnew.FromMM(' + str(key["y"]) + '))\n'
	cmd += 'diode.SetOrientationDegrees(90)\n'
	cmd += 'diode.SetX(pcbnew.FromMM(' + str(key["x"] + 8.5) + '))\n'
	cmd += 'diode.SetY(pcbnew.FromMM(' + str(key["y"] - 5) + '))\n'
	cmd += 'led.SetOrientationDegrees(180)\n'
	cmd += 'led.SetX(pcbnew.FromMM(' + str(key["x"] + 8.975) + '))\n'
	cmd += 'led.SetY(pcbnew.FromMM(' + str(key["y"]) + '))\n'
	cmd += """component.Value().SetVisible(False)
diode.Reference().SetVisible(False)
diode.Value().SetVisible(False)
led.Reference().SetVisible(False)
led.Value().SetVisible(False)
"""
	# Add a Via just under the LED to 5V
	cmd += 'via = pcbnew.PCB_VIA(board)\n'
	cmd += 'board.Add(via)\n'
	cmd += 'via.SetX(pcbnew.FromMM(' + str(key["x"] + 8.325) + '))\n'
	cmd += 'via.SetY(pcbnew.FromMM(' + str(key["y"] + 2) + '))\n'
	cmd += 'via.SetNet(net)\n'
	cmd += """via.SetLayerPair(
    board.GetLayerID('F.Cu'),
    board.GetLayerID('F.Cu')
)
via.SetViaType(pcbnew.VIATYPE_THROUGH)
via.SetWidth(pcbnew.FromMM(0.6))  # VIA diameter in mm
via.SetDrill(pcbnew.FromMM(0.3))  # Drill size in mm
"""

cmd += "pcbnew.Refresh()\n"

print("----- KiCad Script ----")
print(cmd)