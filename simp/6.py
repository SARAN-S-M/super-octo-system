# pip install pgmpy

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

class CourseSuccessPredictor:
    def __init__(self):
        self.model = BayesianNetwork([('Attendance', 'CourseSuccess'), ('Participation', 'CourseSuccess')])
        self._create_cpds()
        self._add_cpds_to_model()

    def _create_cpds(self):
        """Create the conditional probability distributions (CPDs)."""
        self.cpd_attendance = TabularCPD(variable='Attendance', variable_card=2, values=[[0.7], [0.3]])
        self.cpd_participation = TabularCPD(variable='Participation', variable_card=2, values=[[0.6], [0.4]])
        self.cpd_course_success = TabularCPD(variable='CourseSuccess', variable_card=2,
                                             values=[[0.9, 0.7, 0.6, 0.4],
                                                     [0.1, 0.3, 0.4, 0.6]],
                                             evidence=['Attendance', 'Participation'],
                                             evidence_card=[2, 2])

    def _add_cpds_to_model(self):
        """Add the CPDs to the Bayesian network model."""
        self.model.add_cpds(self.cpd_attendance, self.cpd_participation, self.cpd_course_success)
        assert self.model.check_model()

    def get_user_input(self):
        """Prompt the user for attendance and participation levels."""
        try:
            attendance_input = input("Enter Attendance level (0 for Good, 1 for Poor): ")
            participation_input = input("Enter Participation level (0 for High, 1 for Low): ")
            attendance_level = int(attendance_input)
            participation_level = int(participation_input)

            if attendance_level not in [0, 1] or participation_level not in [0, 1]:
                raise ValueError("Attendance and Participation levels must be 0 or 1.")
            return attendance_level, participation_level
        except ValueError as e:
            print(f"Invalid input: {e}")
            return None, None

    def predict_course_success(self, attendance_level, participation_level):
        """Predict the course success based on the user's input."""
        inference = VariableElimination(self.model)
        query_result = inference.query(variables=['CourseSuccess'],
                                       evidence={'Attendance': attendance_level, 'Participation': participation_level})
        return query_result

    def display_results(self, query_result):
        """Display the prediction results."""
        print("\nPrediction Results for Course Success:")
        print("Note: CourseSuccess = 0, CourseFailure = 1")

        for i, prob in enumerate(query_result.values):
            label = "CourseSuccess" if i == 0 else "CourseFailure"
            print(f"{label}: {prob * 100:.2f}%")


if __name__ == "__main__":
    predictor = CourseSuccessPredictor()
    attendance_level, participation_level = predictor.get_user_input()
    
    if attendance_level is not None and participation_level is not None:
        query_result = predictor.predict_course_success(attendance_level, participation_level)
        predictor.display_results(query_result)
