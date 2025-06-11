import tkinter as tk
from tkinter import Toplevel, Label, Scrollbar, Text, RIGHT, Y, BOTH, END


GEOLOGIC_PERIODS = [
    {
        "name": "Precambrian",
        "time": "4,600 - 541 million years ago",
        "events": (
            "- Formation of Earth from dust and gas around the young Sun.\n"
            "- Formation of the Moon likely from a giant impact.\n"
            "- First life appears: simple prokaryotic cells (bacteria and archaea).\n"
            "- Photosynthesis by cyanobacteria begins, releasing oxygen.\n"
            "- Oxygenation of the atmosphere (Great Oxidation Event).\n"
            "- Eukaryotic cells evolve.\n"
            "- First multicellular organisms emerge."
        ),
        "color": "#E24152"
    },
    {
        "name": "Cambrian",
        "time": "541 - 485 million years ago",
        "events": (
            "- Cambrian Explosion: rapid diversification of multicellular life.\n"
            "- Appearance of major animal groups such as arthropods, mollusks, and echinoderms.\n"
            "- Trilobites and brachiopods are abundant.\n"
            "- Early reef-building organisms evolve."
        ),
        "color": "#8BAA78"
    },
    {
        "name": "Ordovician",
        "time": "485 - 443 million years ago",
        "events": (
            "- Diversification of marine invertebrates.\n"
            "- First jawless fish appear.\n"
            "- Large reef systems develop.\n"
            "- Ends with a major glaciation and mass extinction."
        ),
        "color": "#00A78E"
    },
    {
        "name": "Silurian",
        "time": "443 - 419 million years ago",
        "events": (
            "- Recovery from Ordovician extinction.\n"
            "- Jawed fish emerge.\n"
            "- First vascular plants appear on land.\n"
            "- Coral reefs expand."
        ),
        "color": "#B3DDC9"
    },
    {
        "name": "Devonian",
        "time": "419 - 359 million years ago",
        "events": (
            "- Known as the 'Age of Fishes'.\n"
            "- First forests and seed-bearing plants.\n"
            "- Early amphibians emerge.\n"
            "- First insects appear.\n"
            "- Ends with a series of extinction events."
        ),
        "color": "#CE9B59"
    },
    {
        "name": "Carboniferous",
        "time": "359 - 299 million years ago",
        "events": (
            "- Extensive coal-forming forests.\n"
            "- Giant insects and amphibians thrive.\n"
            "- First reptiles evolve.\n"
            "- Oxygen levels reach one of the highest in Earth history."
        ),
        "color": "#63A2A6"
    },
    {
        "name": "Permian",
        "time": "299 - 252 million years ago",
        "events": (
            "- Supercontinent Pangaea forms.\n"
            "- Diversification of amniotes (reptiles, synapsids).\n"
            "- Therapsids (mammal ancestors) dominate.\n"
            "- Ends with the largest mass extinction in Earth’s history."
        ),
        "color": "#E66449"
    },
    {
        "name": "Triassic",
        "time": "252 - 201 million years ago",
        "events": (
            "- First dinosaurs and early mammals appear.\n"
            "- Reptiles dominate terrestrial ecosystems.\n"
            "- Gymnosperms (conifers) dominate plant life.\n"
            "- Ends with an extinction that clears the way for dinosaurs."
        ),
        "color": "#8E52A0"
    },
    {
        "name": "Jurassic",
        "time": "201 - 145 million years ago",
        "events": (
            "- Dinosaurs flourish and diversify.\n"
            "- First birds (e.g. Archaeopteryx) appear.\n"
            "- Large sauropods dominate land.\n"
            "- Breakup of Pangaea continues."
        ),
        "color": "#00B8E6"
    },
    {
        "name": "Cretaceous",
        "time": "145 - 66 million years ago",
        "events": (
            "- Flowering plants (angiosperms) evolve and spread.\n"
            "- Dinosaurs continue to dominate.\n"
            "- Ends with the Cretaceous-Paleogene (K-Pg) extinction event.\n"
            "- Most dinosaurs and many marine species go extinct."
        ),
        "color": "#87C76F"
    },
    {
        "name": "Paleogene",
        "time": "66 - 23 million years ago",
        "events": (
            "- Mammals diversify rapidly in the absence of dinosaurs.\n"
            "- First large mammals and early primates evolve.\n"
            "- Tropical climates and forests widespread."
        ),
        "color": "#F9A76F"
    },
    {
        "name": "Neogene",
        "time": "23 - 2.6 million years ago",
        "events": (
            "- Grasslands spread, driving evolution of grazing mammals.\n"
            "- Appearance of modern mammal and bird species.\n"
            "- Ancestors of humans evolve in Africa."
        ),
        "color": "#FEDC00"
    },
    {
        "name": "Quaternary",
        "time": "2.6 million years ago - Present",
        "events": (
            "- Multiple Ice Ages occur.\n"
            "- Extinction of large mammals (megafauna).\n"
            "- Homo sapiens emerge and spread globally.\n"
            "- Development of agriculture and civilizations."
        ),
        "color": "#F9F97F"
    }
]

def show_period_info(period):
    info_window = Toplevel()
    info_window.title(period["name"])
    info_window.geometry("450x300")

    Label(info_window, text=period["name"], font=("Helvetica", 16, "bold"), bg=period["color"])
    Label(info_window, text=f"Timeframe: {period['time']}", font=("Helvetica", 12)).pack(pady=5)

    text_widget = Text(info_window, wrap='word', font=("Helvetica", 11))
    text_widget.insert(END, f"{period['events']}")
    text_widget.config(state='disabled')
    text_widget.pack(fill=BOTH, expand=True, padx=10, pady=5)

    scrollbar = Scrollbar(info_window, command=text_widget.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_widget.config(yscrollcommand=scrollbar.set)

def main():
    root = tk.Tk()
    root.title("Interactive Geologic Time Scale")
    root.geometry("520x720")

    title = tk.Label(root, text="Geologic Time Scale", font=("Helvetica", 18, "bold"))
    title.pack(pady=10)

    timeline_frame = tk.Frame(root)
    timeline_frame.pack(fill="both", expand=True)

    # Add period buttons (from bottom up)
    for period in reversed(GEOLOGIC_PERIODS):
        button = tk.Button(
            timeline_frame,
            text=period["name"],
            font=("Helvetica", 12),
            bg=period["color"],
            relief="raised",
            width=40,
            height=2,
            command=lambda p=period: show_period_info(p)
        )
        button.pack(pady=2)

    root.mainloop()

if __name__ == '__main__':
    main()
