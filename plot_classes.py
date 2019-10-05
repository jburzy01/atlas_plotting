from ROOT import *
import atlas_style

import os
import math
from sys import argv, exit

from plot_base import *
from plot_util import *

gROOT.SetBatch(kTRUE)
gStyle.SetOptStat(0)
gStyle.SetLineWidth(2)

colors  = [kAzure+5,kViolet+5, kPink+5, kOrange+5, kTeal+5, kRed]
markers = [20, 21, 22, 23, 43, 47] 

class Hist1D(PlotBase):
    def __init__(self, hist_list, file_list, legends, norm = False, **kwargs):

        super(Hist1D, self).__init__(
                legend_loc = [0.6,0.9,0.85, 0.9 - 0.045*(len(file_list)+1) ],
                atlas_loc = [0.175,0.875],
                extra_lines_loc = [0.175,0.775],
                **kwargs)

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

        for h in self.hists:
            if (self.rebin != None):
                h.Rebin(self.rebin)

            self.set_x_axis_bounds(h)
            self.set_titles(h, "Vertices")
            format_for_drawing(h)

            h.SetLineColor( colors[ self.hists.index(h)] )
            h.SetMarkerColor( colors[ self.hists.index(h)] )
            h.SetMarkerStyle( markers[ self.hists.index(h)  ] )
            if(norm == True):
                h.Scale(1.0/h.Integral())

        self.pad_empty_space(self.hists)
        pad1 = self.canvas.cd(1)
        format_simple_pad(pad1)

        pad1.cd()

        if (self.log_scale):
            pad1.SetLogy()

        firstHist = True
        for h in self.hists:
            self.leg.AddEntry(h, legends[ self.hists.index(h)  ], 'lp')
            if firstHist:
                firstHist = False
                h.Draw("hist")
                h.Draw("PE same")
            else:
                h.Draw("hist same")
                h.Draw("PE same")


        if "R" in hist_list[0]:
            self.draw_material_layers()


        self.leg.Draw()

        self.canvas.Update()
        self.canvas.Modified()

        self.print_to_file(self.name + ".pdf")

        pad1.Close()

    def draw_material_layers(self):
        coords = [33.5,50.5,88.5,122.5,299.0]
        for coord in coords:
            line = TLine(coord,0,coord,self.y_max * 1.0/self.empty_scale)
            line.SetLineColor(kRed)
            line.SetLineWidth(2)
            line.SetLineStyle(8)
            line.DrawLine(coord,0,coord,self.y_max * 1.0/self.empty_scale)
            if(coords.index(coord) == 0):
                self.leg.AddEntry(line, "Material Layers", "l")
        
