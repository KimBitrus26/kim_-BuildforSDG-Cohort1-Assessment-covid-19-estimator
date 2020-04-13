

def estimator(data):
  my_input_data = {
    region: {
    name: "Africa",
    avgAge: 19.7,
    avgDailyIncomeInUSD: 5,
    avgDailyIncomePopulation: 0.71
    },
    periodType: "days",
    timeToElapse: 58,
    reportedCases: 674,
    population: 66622705,
    totalHospitalBeds: 1380614
    }

  def convert_to_days():
    if my_input_data["periodType"] == "days":
      coverted_days = my_input_data["timeToElapse"]

    elif my_input_data["periodType"] == "weeks":
      coverted_days = my_input_data["timeToElapse"] * 7

    elif my_input_data["periodType"] == "weeks":
      coverted_days = my_input_data["timeToElapse"] * 30

      return coverted_days 

  return {
    "data" : my_input_data,
    "impact" : {
      "currentlyInfected" : my_input_data["reportedCases"] * 10,
      "infectedByRequestedTime" : (my_input_data["reportedCases"] * 10) * (2 ** (convert_to_days()/3))

          },
    "severeImpact" : {
    "currentlyInfected" : my_input_data["reportedCases"] * 50,
    "infectedByRequestedTime" : (my_input_data["reportedCases"] * 10) * (2 ** (convert_to_days()/3))
  
    }
  } 

