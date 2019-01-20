from src.logs import *
from src.grid import *
import unittest

class testGrid(unittest.TestCase):
    def test_split_is_ok(self):
        result = splitInput(testLog)

        self.assertEqual(result, splittedInput)

    def test_there_is_no_space_in_split_result(self):
        result = splitInput(testLog)

        self.assertNotIn('', result)
        self.assertNotIn(' ', result)

    def test_input_is_a_string(self):
        with self.assertRaises(AttributeError):
            result = splitInput(brokenTestLog)

    def test_get_laps_from_splitted_input(self):
        result = getLaps(splittedInput)

        self.assertEqual(result, laps)

    def test_get_pilot_cod_from_laps(self):
        result = getCodPiloto(laps)

        self.assertEqual(result, pilots_code)

    def test_get_final_infos_on_stop_mode(self):
        result = generateFinalInfosStop(laps)

        self.assertEqual(result, finalInfosStop)

    def test_time_laps_are_in_the_right_format_on_stop_mode(self):
        with self.assertRaises(ValueError):
            result = generateFinalInfosStop(brokenLaps)

    def test_get_final_infos_on_keep_running_mode(self):
        result = generateFinalInfosKeepRunning(laps, pilots_code)

        self.assertEqual(result, finalInfosKeepRunning)

    def test_time_laps_are_in_the_right_format_on_keep_running_mode(self):
        with self.assertRaises(ValueError):
            result = generateFinalInfosKeepRunning(brokenLaps, pilots_code)

    def test_sort_final_infos(self):
        result = sortFinalResult(finalInfosKeepRunning)

        self.assertEqual(result, sortedFinalInfos)

    def test_get_best_lap(self):
        result = getMelhorVoltaDaCorrida(sortedFinalInfos)

        self.assertEqual(result, bestLap)

    def test_get_final_result_on_keep_running_mode(self):
        result = getFinalResultKeepRunning(testLog)

        self.assertEqual(result, finalResultKeepRunning)

    def test_get_final_result_on_stop_mode(self):
        result = getFinalResultStop(testLog)

        self.assertEqual(result, finalResultStop)

if __name__ == '__main__':
    unittest.main()