from model import Occurrence
from model.enum.occurrence import OccurrenceEnum

class OccurrenceMapper:

    @staticmethod
    def values_to_occurrence(values, year, department):
        occurrence = Occurrence()
        occurrence.department = department.split("-")[-1]
        occurrence.year = year
        occurrence.occurrence = OccurrenceEnum(values[0].split("(")[0]).value
        occurrence.jan = values[1]
        occurrence.feb = values[2]
        occurrence.mar = values[3]
        occurrence.apr = values[4]
        occurrence.may = values[5]
        occurrence.jun = values[6]
        occurrence.jul = values[7]
        occurrence.aug = values[8]
        occurrence.sep = values[9]
        occurrence.oct = values[10]
        occurrence.nov = values[11]
        occurrence.dec = values[12]
        occurrence.total = values[13]
        return occurrence