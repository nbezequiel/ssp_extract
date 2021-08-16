from model import Occurrence

class OccurrenceMapper:

    @staticmethod
    def values_to_occurrence(values, year, department):
        occurrence = Occurrence()
        occurrence.department_name = department
        occurrence.year = year
        occurrence.crime = values[0]
        occurrence.jan = values[1]
        occurrence.feb = values[2]
        occurrence.mar = values[3]
        occurrence.apr = values[4]
        occurrence.may = values[5]
        occurrence.jun = values[6]
        occurrence.jul = values[7]
        occurrence.aug = values[8]
        occurrence.sep = values[9]
        occurrence.otu = values[10]
        occurrence.nov = values[11]
        occurrence.dec = values[12]
        occurrence.total = values[13]
        return occurrence