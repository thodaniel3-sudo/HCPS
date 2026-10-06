# ==========================================================
# HYBRID COMPOSITE PREDICTION SYSTEM (HCPS)
# comparison.py
#
# Experimental vs Predicted Property Comparison Module
# Compatible with main.py
# ==========================================================



def compare_properties(experimental, predicted):
    """
    Compare experimental and predicted properties.
    """


    results = {}



    for property_name in predicted:


        exp_value = experimental.get(
            property_name,
            0
        )


        pred_value = predicted.get(
            property_name,
            0
        )



        if exp_value != 0:

            percentage_error = abs(
                (pred_value - exp_value)
                /
                exp_value
            ) * 100

        else:

            percentage_error = 0



        accuracy = 100 - percentage_error


        if accuracy < 0:

            accuracy = 0



        results[property_name] = {


            "Experimental":
                round(
                    exp_value,
                    3
                ),



            "Predicted":
                round(
                    pred_value,
                    3
                ),



            "Percentage Error (%)":
                round(
                    percentage_error,
                    3
                ),



            "Accuracy (%)":
                round(
                    accuracy,
                    3
                )

        }



    return results





def compare_result(experimental, predicted):
    """
    Single comparison compatibility function.
    """

    return compare_properties(
        experimental,
        predicted
    )







def compare_multiple(experimental_list, predicted_list):
    """
    Compare multiple composite samples.

    Parameters:
        experimental_list:
            List of experimental dictionaries

        predicted_list:
            List of predicted dictionaries

    Returns:
        List of comparison results
    """


    results = []



    for experimental, predicted in zip(
            experimental_list,
            predicted_list
    ):


        result = compare_properties(
            experimental,
            predicted
        )


        results.append(result)



    return results





def calculate_accuracy(results):
    """
    Calculate average prediction accuracy.
    """


    if not results:

        return 0



    accuracy_values = []



    for prop in results:


        accuracy_values.append(

            results[prop].get(
                "Accuracy (%)",
                0
            )

        )



    average = sum(
        accuracy_values
    ) / len(
        accuracy_values
    )



    return round(
        average,
        3
    )






def generate_comparison_summary(results):
    """
    Generate readable comparison report.
    """


    summary = ""



    for prop, data in results.items():


        summary += (

            f"{prop}\n"

            f"Experimental: "
            f"{data['Experimental']}\n"

            f"Predicted: "
            f"{data['Predicted']}\n"

            f"Error: "
            f"{data['Percentage Error (%)']}%\n"

            f"Accuracy: "
            f"{data['Accuracy (%)']}%\n\n"

        )



    return summary