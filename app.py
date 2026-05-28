import gradio as gr
import pickle

model = pickle.load(open("pricing_model.pkl", "rb"))

def predict_price(demand, inventory, competitor_price, season):

    season_map = {
        "Normal": 1,
        "Festival": 2,
        "Holiday": 3
    }

    result = model.predict([[
        demand,
        inventory,
        competitor_price,
        season_map[season]
    ]])

    return f"Recommended Price: ₹{round(result[0], 2)}"

demo = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Slider(0, 100, label="Demand"),
        gr.Slider(0, 500, label="Inventory"),
        gr.Number(label="Competitor Price"),
        gr.Dropdown(
            ["Normal", "Festival", "Holiday"],
            label="Season"
        )
    ],
    outputs="text",
    title="💸 AI Dynamic Pricing Engine",
    description="Predict smart product pricing using AI."
)

demo.launch()