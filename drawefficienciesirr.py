import csv
import ROOT

stubsplot = ROOT.TGraph()
pixelplot = ROOT.TGraph()
stripplot = ROOT.TGraph()
pixelplot = ROOT.TGraph()
realstripplot = ROOT.TGraph()

with open('combinedirr.csv', 'r') as file:
    reader = csv.reader(file)
    
    i = 0
    for row in reader:
        stubsplot.SetPoint(i,float(row[0]),float(row[3]))
        pixelplot.SetPoint(i,float(row[0]),float(row[2]))
        realstripplot.SetPoint(i,float(row[1]),float(row[4]))
        i += 1

stubsymax = stubsplot.GetYaxis().GetXmax()
stubsymin = stubsplot.GetYaxis().GetXmin()
stubsxmin = stubsplot.GetXaxis().GetXmin()
stubsxmax = stubsplot.GetXaxis().GetXmax()
stripxmin = realstripplot.GetXaxis().GetXmin()
stripxmax = realstripplot.GetXaxis().GetXmax()
stubrange = stubsplot.GetXaxis().GetXmax() - stubsplot.GetXaxis().GetXmin()
striprange =  realstripplot.GetXaxis().GetXmax() - realstripplot.GetXaxis().GetXmin()
    
with open('combinedirr.csv', 'r') as file2:
    reader2 = csv.reader(file2)
    i = 0

    for row in reader2:
        stripplot.SetPoint(i,((float(row[1])) - stripxmin) * stubrange / striprange + stubsxmin,float(row[4]))
        i +=1
    
canvas = ROOT.TCanvas("canvas", "", 800, 600)

stubsplot.GetYaxis().SetTitle("Efficiency (%)")
stubsplot.SetMarkerSize(6)
pixelplot.SetMarkerSize(6)
stripplot.SetMarkerSize(6)
stubsplot.SetLineWidth(0)
pixelplot.SetLineWidth(0)
stripplot.SetLineWidth(0)
pixelplot.SetMarkerColor(ROOT.kAzure)
stripplot.SetMarkerColor(ROOT.kRed)
stubsplot.SetMarkerColor(ROOT.kViolet)

stubsplot.Draw("AP")
pixelplot.Draw("P")
stripplot.Draw("P")

stripaxis = ROOT.TGaxis(stubsxmin, stubsymax ,stubsxmax,stubsymax, stripxmin, stripxmax, 510, "-")
stripaxis.SetLabelSize(.035)
stripaxis.SetLabelOffset(-.005)
stripaxis.Draw()

leg = ROOT.TLegend(.7,.45, .95, .7)
leg.AddEntry(pixelplot, "Pixel Efficiency")
leg.AddEntry(stripplot, "Strip Efficiency")
leg.AddEntry(stubsplot, "Stub Efficiency")
leg.Draw()

text1 = ROOT.TText(.85*stubsxmax, 1.06* stubsymax,"Strip")
text1.SetTextSize(0.04)
text1.SetTextColor(ROOT.kRed)
text1.Draw()

text2 = ROOT.TText(.903*stubsxmax, 1.06*stubsymax,"Threshold")
text2.SetTextSize(0.04)
text2.Draw()

text3 = ROOT.TText(.79*stubsxmax,stubsymin - (.1*stubsymax),"Stub/")
text3.SetTextSize(0.04)
text3.SetTextColor(ROOT.kViolet)
text3.Draw()

text4 = ROOT.TText(.843*stubsxmax,stubsymin - (.1*stubsymax),"Pixel")
text4.SetTextSize(0.04)
text4.SetTextColor(ROOT.kAzure)
text4.Draw()

text5 = ROOT.TText(.9*stubsxmax,stubsymin - (.1*stubsymax),"Threshold")
text5.SetTextSize(0.04)
text5.Draw()


canvas.Update()
canvas.SaveAs("ThScanPlotIrr.png")
print("The plot for the irradiated threshold scan has been drawn as ThScanPlotIrr.png")

