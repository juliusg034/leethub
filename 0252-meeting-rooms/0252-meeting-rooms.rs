use std::collections::HashMap;
impl Solution {
    pub fn can_attend_meetings(mut intervals: Vec<Vec<i32>>) -> bool {

        intervals.sort_by_key(|interval| interval[0]);

        for i in 1..intervals.len() {
            let prev_end = intervals[i-1][1];
            let curr_start = intervals[i][0];

            if curr_start < prev_end {
                return false
            }
        }

        return true
    }
}