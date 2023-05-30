def writeln(fh, text):
    fh.write(text)
    fh.write("\n")


styles = ["border", "border-t", "border-r", "border-l", "border-b", "text", "bg"]
colours = ["gray", "slate", "zinc", "neutral", "stone", "red", "orange", "amber", "yellow", "lime", "green", "emerald",
           "teal", "cyan", "sky", "blue", "indigo", "violet", "purple", "fuchsia", "pink", "rose", ]
values = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
percentage = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

fh = open("app/templates/auto-all.html", "w")
for colour in colours:
    for style in styles:
        for value in values:
            s = (f"<div class='{style}-{colour}-{value}'></div>")
            writeln(fh, s)

styles = ["opacity"]
percentage = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
for style in styles:
    for value in percentage:
        s = (f"<div class='{style}-{value}'></div>")
        writeln(fh, s)

spacing = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56,
           60, 64, 72, 80, 96, ]

aspects = ["aspect-auto", "aspect-square", "aspect-video", ]

containers = ["sm", "md", "lg", "xl", "2xl", ]
breakpoints = ["sm:", "md:", "lg:", "xl:", "2xl:", ""]
for value in containers:
    for bp in breakpoints:
        s = (f"<div class='{bp}container-{value}'></div>")
        writeln(fh, s)

columns = ["columns-1", "columns-2", "columns-3", "columns-4", "columns-5", "columns-6", "columns-7", "columns-8",
           "columns-9", "columns-10", "columns-11", "columns-12", "columns-auto", "columns-3xs", "columns-2xs",
           "columns-xs", "columns-sm", "columns-md", "columns-lg", "columns-xl", "columns-2xl", "columns-3xl",
           "columns-4xl", "columns-5xl", "columns-6xl", "columns-7xl", ]
breakpoints = ["sm:", "md:", "lg:", "xl:", "2xl:", ""]
for item in columns:
    for bp in breakpoints:
        s = (f"<div class='{bp}{item}'></div>")
        writeln(fh, s)

breakafter =["break-after-auto","break-after-avoid","break-after-all","break-after-avoid-page","break-after-page","break-after-left","break-after-right","break-after-column",]
states=["hover:","focus:","active:",""]
for item in breakafter:
    for state in states:
        s = (f"<div class='{state}{item}'></div>")
        writeln(fh, s)


# --- close ---
fh.close()
