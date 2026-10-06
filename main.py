
"""
==========================================================

main.py

Hybrid Composite System (HCPS)

Main Controller

Author: Daniel Thomas

==========================================================
"""


# ==========================================================
# STANDARD PYTHON IMPORTS
# ==========================================================

import tkinter as tk
from tkinter import messagebox


# ==========================================================
# AI REPORT
# ==========================================================

from ai_report import generate_ai_report


# ==========================================================
# USER INTERFACE MODULE
# ==========================================================

from interface import (
    create_window,
    create_title,
    create_input_frame,
    create_entries,
    create_buttons,
    create_status_bar,
    update_status,
    clear_entries,
    show_results,
    show_error,
)


# ==========================================================
# ENGINEERING CALCULATIONS MODULE
# ==========================================================

from calculations import (
    validate_percentages,
    composite_density,
    weight_fractions,
    rule_of_mixtures_calculation,
    percentage_error,
    prediction_accuracy,
    penetration_index,
    optimum_sample,
)


# ==========================================================
# VALIDATION MODULE
# ==========================================================

from validation import (
    validate_all,
)


# ==========================================================
# MACHINE LEARNING MODULE
# ==========================================================

from machine_learning import (
    HCPS_AI,
)


# ==========================================================
# DATA LOADER MODULE
# ==========================================================

from dataset_loader import (
    prepare_training_data,
)


# ==========================================================
# DATABASE MODULE
# ==========================================================

from database import (
    create_table,
    save_sample,
)


# ==========================================================
# AI STATUS MODULE
# ==========================================================

from ai_status import (
    get_ai_status,
)


# ==========================================================
# CONSTANTS
# ==========================================================

TOTAL_VOLUME = 104.0


# ==========================================================
# HCPS DATA STORAGE
# ==========================================================

hcps_data = {

    "density": None,

    "prediction": None,

    "comparison": None,

    "experimental": None,

    "epoxy": None,

    "horn": None,

    "cotton": None,

    "limestone": None,

}


# ==========================================================
# AI MODEL INITIALIZATION
# ==========================================================

ai_model = HCPS_AI()


try:

    X_train, y_train = prepare_training_data()

    ai_model.train(
        X_train,
        y_train
    )

    print(
        "HCPS AI MODEL TRAINED SUCCESSFULLY"
    )

except Exception as e:

    print(
        "AI Training Error:",
        e
    )


# ==========================================================
# CALCULATE FUNCTION
# ==========================================================

def calculate():

    try:

        # ==================================================
        # READ ALL INPUT VALUES
        # ==================================================

        values = []

        for entry in entries:

            text = entry.get().strip()

            if text == "":
                raise ValueError(
                    "All input fields must be completed."
                )

            values.append(
                float(text)
            )


        # ==================================================
        # CHECK INPUT COUNT
        # ==================================================

        if len(values) < 8:

            show_error(
                "Please enter all 8 required input values."
            )

            return


        # ==================================================
        # MATERIAL DENSITIES
        # ==================================================

        epoxy_density = values[0]

        horn_density = values[1]

        cotton_density = values[2]

        limestone_density = values[3]


        # ==================================================
        # COMPOSITION VOLUME PERCENTAGES
        # ==================================================

        epoxy_percent = values[4]

        horn_percent = values[5]

        cotton_percent = values[6]

        limestone_percent = values[7]


        # ==================================================
        # CHECK DENSITIES
        # ==================================================

        densities = [

            epoxy_density,

            horn_density,

            cotton_density,

            limestone_density

        ]

        for density_value in densities:

            if density_value <= 0:

                show_error(
                    "All material densities must be greater than zero."
                )

                return


        # ==================================================
        # VALIDATE COMPOSITION PERCENTAGES
        # ==================================================

        valid, total = validate_percentages(

            epoxy_percent,

            horn_percent,

            cotton_percent,

            limestone_percent

        )


        if not valid:

            show_error(

                "Formulation percentages must equal 100%.\n\n"

                f"Current total = {total:.3f}%\n\n"

                "Please check the epoxy, cow horn, cotton wool, "
                "and limestone percentages."

            )

            return


        # ==================================================
        # VALIDATE PERCENTAGE RANGES
        # ==================================================

        percentages = [

            epoxy_percent,

            horn_percent,

            cotton_percent,

            limestone_percent

        ]

        for percentage in percentages:

            if percentage < 0 or percentage > 100:

                show_error(
                    "Each composition percentage must be "
                    "between 0% and 100%."
                )

                return


        # ==================================================
        # RULE OF MIXTURES CALCULATION
        #
        # CONSTANT TOTAL COMPOSITE VOLUME = 104 cm³
        #
        # The input percentages are VOLUME percentages.
        #
        # Formula:
        #
        # ρc = Veρe + Vhρh + Vcρc + Vlρl
        #
        # ==================================================

        result_data = rule_of_mixtures_calculation(

            epoxy_density,

            horn_density,

            cotton_density,

            limestone_density,

            epoxy_percent,

            horn_percent,

            cotton_percent,

            limestone_percent,

            total_volume=TOTAL_VOLUME

        )


        # ==================================================
        # EXTRACT CALCULATION RESULTS
        # ==================================================

        volumes = result_data["volumes"]

        masses = result_data["masses"]

        total_volume = result_data["total_volume"]

        total_mass = result_data["total_mass"]

        density = result_data["theoretical_density"]

        direct_density = result_data[
            "direct_rule_of_mixtures_density"
        ]


        # ==================================================
        # VERIFY THE TWO CALCULATION METHODS
        # ==================================================

        density_difference = abs(
            density - direct_density
        )


        # ==================================================
        # STORE DATA
        # ==================================================

        hcps_data["density"] = density

        hcps_data["epoxy"] = epoxy_percent

        hcps_data["horn"] = horn_percent

        hcps_data["cotton"] = cotton_percent

        hcps_data["limestone"] = limestone_percent


        # ==================================================
        # DISPLAY COMPLETE RESULT
        # ==================================================

        result = (

            "HCPS RULE OF MIXTURES RESULT\n"

            "========================================\n\n"


            "INPUT FORMULATION\n"

            "----------------------------------------\n"

            f"Epoxy       : {epoxy_percent:.2f}%\n"

            f"Cow Horn    : {horn_percent:.2f}%\n"

            f"Cotton Wool : {cotton_percent:.2f}%\n"

            f"Limestone   : {limestone_percent:.2f}%\n"

            f"Total       : {total:.2f}%\n\n"


            "CONSTANT COMPOSITE VOLUME\n"

            "----------------------------------------\n"

            f"{total_volume:.2f} cm³\n\n"


            "CONSTITUENT VOLUMES\n"

            "----------------------------------------\n"

            f"Epoxy       : "
            f"{volumes['Epoxy']:.4f} cm³\n"

            f"Cow Horn    : "
            f"{volumes['Cow Horn']:.4f} cm³\n"

            f"Cotton Wool : "
            f"{volumes['Cotton']:.4f} cm³\n"

            f"Limestone   : "
            f"{volumes['Limestone']:.4f} cm³\n\n"


            "CONSTITUENT MASSES\n"

            "----------------------------------------\n"

            f"Epoxy       : "
            f"{masses['Epoxy']:.4f} g\n"

            f"Cow Horn    : "
            f"{masses['Cow Horn']:.4f} g\n"

            f"Cotton Wool : "
            f"{masses['Cotton']:.4f} g\n"

            f"Limestone   : "
            f"{masses['Limestone']:.4f} g\n\n"


            "TOTAL MASS\n"

            "----------------------------------------\n"

            f"{total_mass:.4f} g\n\n"


            "THEORETICAL COMPOSITE DENSITY\n"

            "----------------------------------------\n"

            f"{density:.5f} g/cm³\n\n"


            "DIRECT RULE OF MIXTURES CHECK\n"

            "----------------------------------------\n"

            f"{direct_density:.5f} g/cm³\n\n"


            "CALCULATION VERIFICATION\n"

            "----------------------------------------\n"

            f"Difference = "
            f"{density_difference:.10f} g/cm³\n\n"


            "CALCULATION METHOD\n"

            "----------------------------------------\n"

            "Direct Rule of Mixtures using volume fractions.\n"

            "Theoretical density = Total mass / Total volume.\n"

            "Total composite volume = 104 cm³."

        )


        show_results(

            "Rule of Mixtures Calculation",

            result

        )


        update_status(

            status,

            "Status : Rule of Mixtures Calculation Completed"

        )


    except ValueError as e:

        show_error(

            f"Calculation Input Error:\n\n{str(e)}"

        )


    except Exception as e:

        show_error(

            f"Calculation Error:\n\n{str(e)}"

        )


# ==========================================================
# PREDICT FUNCTION
# ==========================================================

def predict():

    try:

        # ==================================================
        # READ INPUT VALUES
        # ==================================================

        values = []

        for entry in entries:

            text = entry.get().strip()

            if text == "":
                raise ValueError(
                    "All input fields must be completed."
                )

            values.append(
                float(text)
            )


        # ==================================================
        # CHECK INPUT COUNT
        # ==================================================

        if len(values) < 8:

            show_error(

                "Please enter all 8 required input values."

            )

            return


        # ==================================================
        # MATERIAL DENSITIES
        # ==================================================

        epoxy_density = values[0]

        horn_density = values[1]

        cotton_density = values[2]

        limestone_density = values[3]


        # ==================================================
        # COMPOSITION PERCENTAGES
        # ==================================================

        epoxy_percent = values[4]

        horn_percent = values[5]

        cotton_percent = values[6]

        limestone_percent = values[7]


        # ==================================================
        # VALIDATE FORMULATION
        # ==================================================

        valid, total = validate_percentages(

            epoxy_percent,

            horn_percent,

            cotton_percent,

            limestone_percent

        )


        if not valid:

            show_error(

                "Formulation percentages must equal 100%.\n\n"

                f"Current total = {total:.2f}%"

            )

            return


        # ==================================================
        # AI INPUT
        # ==================================================

        ai_input = [

            epoxy_percent,

            horn_percent,

            cotton_percent,

            limestone_percent

        ]


        # ==================================================
        # CHECK AI MODEL
        # ==================================================

        if not ai_model.is_trained():

            show_error(

                "AI model is not trained."

            )

            return


        # ==================================================
        # AI PREDICTION
        # ==================================================

        ai_prediction = ai_model.predict(

            ai_input

        )


        # ==================================================
        # DEBUG AI OUTPUT
        # ==================================================

        print("\nAI RAW OUTPUT")

        print("----------------")

        print(ai_prediction)


        # ==================================================
        # CHECK AI OUTPUT
        # ==================================================

        if len(ai_prediction) < 4:

            show_error(

                "The AI model did not return all required "
                "prediction properties."

            )

            return


        # ==================================================
        # FORMAT AI PREDICTIONS
        # ==================================================

        predictions = {

            "Composite Density (g/cm³)":

                round(

                    float(ai_prediction[0]),

                    3

                ),

            "Flexural Strength (MPa)":

                round(

                    float(ai_prediction[1]),

                    3

                ),
                "Flexural Modulus (GPa)":

                round(

                    float(ai_prediction[2]),

                    3

                ),

            "Compressive Strength (MPa)":

                round(

                    float(ai_prediction[3]),

                    3

                ),

            "Impact Strength (kJ/m²)":

                round(

                    float(ai_prediction[4]),

                    3

                )

        }


        # ==================================================
        # STORE PREDICTION
        # ==================================================

        hcps_data["prediction"] = predictions

        hcps_data["density"] = float(

            ai_prediction[0]

        )

        hcps_data["epoxy"] = epoxy_percent

        hcps_data["horn"] = horn_percent

        hcps_data["cotton"] = cotton_percent

        hcps_data["limestone"] = limestone_percent


        # ==================================================
        # DISPLAY RESULT
        # ==================================================

        result = (

            "HCPS AI PREDICTION RESULTS\n"

            "========================================\n\n"


            "FORMULATION\n"

            "----------------------------------------\n"

            f"Epoxy       : {epoxy_percent:.2f}%\n"

            f"Cow Horn    : {horn_percent:.2f}%\n"

            f"Cotton Wool : {cotton_percent:.2f}%\n"

            f"Limestone   : {limestone_percent:.2f}%\n"

            f"Total       : {total:.2f}%\n\n"


            "AI PREDICTED PROPERTIES\n"

            "----------------------------------------\n"

        )


        for key, value in predictions.items():

            result += (

                f"{key}: {value}\n"

            )


        # ==================================================
        # DISPLAY RESULTS
        # ==================================================

        show_results(

            "Prediction Results",

            result

        )


        # ==================================================
        # UPDATE STATUS
        # ==================================================

        update_status(

            status,

            "Status : AI Prediction Completed"

        )


    except ValueError as e:

        show_error(

            f"Prediction Input Error:\n\n{str(e)}"

        )


    except Exception as e:

        show_error(

            f"Prediction Error:\n\n{str(e)}"

        )


# ==========================================================
# AI MODEL PERFORMANCE FUNCTION
# ==========================================================

def ai_performance():

    try:

        X, y = prepare_training_data()


        if not ai_model.is_trained():

            show_error(

                "AI model is not trained."

            )

            return


        report = generate_ai_report(

            ai_model.model,

            X,

            y

        )


        result = (

            "HCPS AI PERFORMANCE REPORT\n"

            "========================================\n\n"

        )


        for key, value in report.items():

            result += (

                f"{key}: {value}\n"

            )


        show_results(

            "AI Performance",

            result

        )


        update_status(

            status,

            "Status : AI Performance Report Generated"

        )


    except Exception as e:

        show_error(

            f"AI Performance Error:\n\n{str(e)}"

        )


# ==========================================================
# GRAPH FUNCTION
# ==========================================================

def graph():

    try:

        if hcps_data["prediction"] is None:

            show_error(

                "Please run prediction first."

            )

            return


        from graphs import plot_graph


        plot_graph(

            hcps_data["density"],

            hcps_data["epoxy"],

            hcps_data["horn"],

            hcps_data["cotton"],

            hcps_data["limestone"],

            hcps_data["prediction"]

        )


        update_status(

            status,

            "Status : Graph Generated"

        )


    except Exception as e:

        show_error(

            f"Graph Error:\n\n{str(e)}"

        )


# ==========================================================
# COMPARE FUNCTION
# ==========================================================

def compare():

    try:

        if hcps_data["prediction"] is None:

            show_error(

                "Please run prediction before comparison."

            )

            return


        predicted = hcps_data["prediction"]


        window = tk.Toplevel(root)

        window.title(

            "HCPS Experimental Comparison"

        )

        window.geometry(

            "550x600"

        )


        title = tk.Label(

            window,

            text="Enter Experimental Results",

            font=("Arial", 14, "bold")

        )

        title.pack(

            pady=15

        )


        properties = [

            "Flexural Strength (MPa)",

            "Compressive Strength (MPa)",

            "Flexural Modulus (GPa)",


            "Impact Strength (kJ/m²)",

        ]


        experimental_entries = {}


        for prop in properties:

            frame = tk.Frame(window)

            frame.pack(

                pady=5

            )


            label = tk.Label(

                frame,

                text=prop,

                width=28,

                anchor="w"

            )

            label.pack(

                side="left"

            )


            entry = tk.Entry(

                frame,

                width=15

            )

            entry.pack(

                side="right"

            )


            experimental_entries[prop] = entry


        def run_comparison():

            try:

                experimental = {}


                for prop in properties:

                    text = experimental_entries[prop].get().strip()

                    if text == "":

                        raise ValueError(

                            f"Please enter a value for {prop}."

                        )

                    experimental[prop] = float(text)


                from comparison import compare_properties


                results = compare_properties(

                    experimental,

                    predicted

                )


                hcps_data["experimental"] = experimental

                hcps_data["comparison"] = results


                show_comparison_results(

                    results

                )


                window.destroy()


            except ValueError as e:

                messagebox.showerror(

                    "Input Error",

                    str(e)

                )


            except Exception as e:

                messagebox.showerror(

                    "Comparison Error",

                    str(e)

                )


        button = tk.Button(

            window,

            text="Run Comparison",

            command=run_comparison,

            width=20

        )

        button.pack(

            pady=20

        )


    except Exception as e:

        show_error(

            f"Comparison Error:\n\n{str(e)}"

        )


# ==========================================================
# SHOW COMPARISON RESULTS WINDOW
# ==========================================================

def show_comparison_results(results):

    window = tk.Toplevel(root)

    window.title(

        "HCPS Comparison Report"

    )

    window.geometry(

        "900x600"

    )


    frame = tk.Frame(window)

    frame.pack(

        fill="both",

        expand=True

    )


    scrollbar = tk.Scrollbar(frame)

    scrollbar.pack(

        side="right",

        fill="y"

    )


    text = tk.Text(

        frame,

        font=("Consolas", 11),

        yscrollcommand=scrollbar.set

    )

    text.pack(

        side="left",

        fill="both",

        expand=True

    )


    scrollbar.config(

        command=text.yview

    )


    report_text = (

        "HYBRID COMPOSITE PREDICTION SYSTEM (HCPS)\n"

        "==========================================\n\n"

        "EXPERIMENTAL VS PREDICTED COMPARISON\n"

        "==========================================\n\n"

    )


    for prop, data in results.items():

        report_text += (

            f"{prop}\n"

            f"{'-' * 50}\n"

            f"Experimental Value : "
            f"{data['Experimental']}\n"

            f"Predicted Value    : "
            f"{data['Predicted']}\n"

            f"Error (%)          : "
            f"{data['Percentage Error (%)']}\n"

            f"Accuracy (%)       : "
            f"{data['Accuracy (%)']}\n\n"

        )


    text.insert(

        "1.0",

        report_text

    )


    text.config(

        state="disabled"

    )


# ==========================================================
# REPORT FUNCTION
# ==========================================================

def report():

    try:

        if hcps_data["prediction"] is None:

            show_error(

                "Please run prediction before creating report."

            )

            return


        from reports import create_report


        files = create_report(

            hcps_data

        )


        messagebox.showinfo(

            "HCPS Report Generated",

            "Report successfully created:\n\n"

            f"{files[0]}\n"

            f"{files[1]}"

        )


        update_status(

            status,

            "Status : Report Generated"

        )


    except Exception as e:

        show_error(

            f"Report Error:\n\n{str(e)}"

        )


# ==========================================================
# AI STATUS DISPLAY FUNCTION
# ==========================================================

def show_ai_status():

    try:

        ai_status = get_ai_status(

            ai_model

        )


        result = (

            "HCPS ARTIFICIAL INTELLIGENCE STATUS\n"

            "==================================\n\n"

            f"Model: "
            f"{ai_status['Model']}\n\n"

            f"Training Samples: "
            f"{ai_status['Training Samples']}\n\n"

            f"Input Variables: "
            f"{ai_status['Input Variables']}\n\n"

            f"Output Properties: "
            f"{ai_status['Output Properties']}\n\n"

            f"R² Accuracy: "
            f"{ai_status['R2 Accuracy']}\n\n"

            f"System Status: "
            f"{ai_status['Status']}"

        )


        show_results(

            "AI Status",

            result

        )


    except Exception as e:

        show_error(

            f"AI Status Error:\n\n{str(e)}"

        )


# ==========================================================
# RESET FUNCTION
# ==========================================================

def reset():

    try:

        clear_entries(

            entries

        )


        for key in hcps_data:

            hcps_data[key] = None


        update_status(

            status,

            "Status : Ready"

        )


    except Exception as e:

        show_error(

            f"Reset Error:\n\n{str(e)}"

        )


# ==========================================================
# CREATE HCPS APPLICATION WINDOW
# ==========================================================

root = create_window()


# ==========================================================
# CREATE TITLE
# ==========================================================

create_title(

    root

)


# ==========================================================
# CREATE INPUT FRAME
# ==========================================================

input_frame = create_input_frame(

    root

)


# ==========================================================
# CREATE INPUT ENTRIES
# ==========================================================

entries = create_entries(

    input_frame

)


# ==========================================================
# CREATE STATUS BAR
# ==========================================================

status = create_status_bar(

    root

)


# ==========================================================
# CREATE DATABASE TABLE
# ==========================================================

try:

    create_table()

except Exception as e:

    print(

        "Database initialization warning:",

        e

    )


# ==========================================================
# CREATE BUTTONS
# ==========================================================

create_buttons(

    root,

    calculate,

    predict,

    compare,

    graph,

    report,

    reset,

    show_ai_status

)


# ==========================================================
# START HCPS SOFTWARE
# ==========================================================

print()
print("==============================================")
print(" HYBRID COMPOSITE PREDICTION SYSTEM (HCPS)")
print("==============================================")
print()
print("Total composite volume:", TOTAL_VOLUME, "cm³")
print("Calculation method: Direct Rule of Mixtures")
print("Volume fraction basis: YES")
print()


root.mainloop()