from plot_base import *
from plot_util import format_simple_pad, format_for_drawing
from ROOT import gROOT, TFile


class Hist1D(PlotBase):  

  def __init__(
    self,
    hist_list = [],
    file_list = [],
    ratio = False,
    **kwargs):

    super(Hist1D, self).__init__(
      **kwargs)

    self.hist_list = hist_list
    self.file_list = file_list

    if(not len(hist_list)):
      raise Exception("No histogram names provided!")
    if(not len(file_list)):
      raise Exception("No file names provided!")
    if(len(hist_list) > 1 and len(file_list) > 1):
      raise Exception("Please provide either a list of histograms OR a list of files!")

    self.hists = []
    self.files = []

    for f in file_list:
      FILE = TFile.Open(f, "READ")
      self.files.append(FILE)
      for h in hist_list:
        self.hists.append(FILE.Get(h))


    if(not ratio):
      pad = self.canvas.cd(1)
      format_simple_pad(pad)

      pad.cd()


    self.pad_empty_space(self.hists)

    for hist in self.hists:
      if(self.x_units != ""):
        hist.GetXaxis().SetTitle(self.x_title + " [" + self.x_units + "]")
      else:
        hist.GetXaxis().SetTitle(self.x_title)

      hist.GetYaxis().SetTitle(self.y_title)

      format_for_drawing(hist)
      hist.Draw()

    self.print_to_file("test.pdf")



