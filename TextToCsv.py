import csv
import wx
class main(wx.Frame):
	def __init__(self):
		super().__init__(None, title="TextToCsv")
		self.Centre()
		p = wx.Panel(self)
		wx.StaticText(p, -1, "Text")
		self.edit = wx.TextCtrl(p, -1, value="", name="", style=wx.TE_MULTILINE + wx.HSCROLL)
		wx.StaticText(p, -1, "File name")
		self.edit1 = wx.TextCtrl(p, -1)
		generate = wx.Button(p, -1, label="&Save")
		generate.Bind(wx.EVT_BUTTON, self.onGenerate)
		self.Show()
	def onGenerate(self, event):
		if self.edit.GetValue() == "":
			wx.MessageBox("Please enter text", "Error")
			self.SetFocus(self.edit)
		else:
			with open(f"{self.edit1.GetValue()}.csv", "w", newline="") as CSV:
				writer = csv.writer(CSV)
				writer.writerow(self.edit.GetValue().split("\n"))
				self.edit.Value = ""
app=wx.App()
w=main()
w.Show()
app.MainLoop()