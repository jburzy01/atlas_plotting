import ROOT as rt
from math import *
import array as arr
import os
import random
import string

def set_style_ratio(hist, y_title = "Data/Pred.", y_min = 0.5, y_max = 1.5):
     hist.GetYaxis().SetRangeUser(y_min, y_max)
     hist.GetYaxis().SetNdivisions(504, 0)
     hist.GetYaxis().SetTitle(y_title)
     hist.GetYaxis().CenterTitle()

def format_for_drawing(histo):
    histo.GetXaxis().SetTitleOffset(1.2);
    histo.GetYaxis().SetTitleOffset(1.35);
    histo.GetXaxis().SetTitleSize(.045);
    histo.GetYaxis().SetTitleSize(.045);
    histo.GetXaxis().SetLabelSize(.05);
    histo.GetXaxis().SetLabelOffset(0.01);
    histo.GetYaxis().SetLabelSize(.045);
    histo.GetYaxis().SetMaxDigits(4);


def format_simple_pad(pad):
    pad.SetPad(0.0, 0.0, 1., 1.)
    pad.SetTopMargin(0.065)
    pad.SetRightMargin(0.06)
    pad.SetLeftMargin(0.13)
    pad.SetBottomMargin(0.15)
#    pad.SetFillColorAlpha(0, 0.)
    pad.SetBorderSize(0)
    pad.SetGridy(0)
    pad.SetBorderSize(0)

def format_2pads_for_ratio():
    pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetTopMargin(0.03)
    pad1.SetRightMargin(0.03)
    pad1.SetLeftMargin(0.11)
    pad1.SetBottomMargin(0.03)
    pad1.SetFillColorAlpha(0, 0.)
    pad1.SetBorderSize(0)
    pad1.SetGridy(0)
    pad1.SetBorderSize(0)

    pad2 = TPad("pad2", "pad2", 0, 0.02, 1, 0.3)
    pad2.SetTopMargin(0.0)
    pad2.SetRightMargin(0.03)
    pad2.SetLeftMargin(0.11)
    pad2.SetBottomMargin(0.45)
    pad2.SetFillColorAlpha(0, 0.)
    pad2.SetBorderSize(0)
    pad2.SetGridy(0)
    pad2.SetBorderSize(0)

    return pad1, pad2

def draw_hists(hlist, options):
    assert(len(hlist) > 0)

    hlist[0].Draw(options)
    for i in range(len(hlist)):
        hlist[i].Draw(options + ",same")


