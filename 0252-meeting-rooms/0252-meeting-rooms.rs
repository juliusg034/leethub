use std::collections::HashMap;
impl Solution {
    pub fn can_attend_meetings(intervals: Vec<Vec<i32>>) -> bool {

        /* Psuedo code:

            checking meeting time start/end
            check hashmap else add to hashmap

            if in hashmap:
                check if time conflicts:
                    return false
                else
                    continue
         */
        
        let mut map = HashMap::new();
            for interval in intervals {
                let start = interval[0];
                let end = interval[1];

                for num in start..end {
                    if map.contains_key(&num) {
                        return false
                    }
                    map.insert(num, true);
                }
            }

            true
    }
}