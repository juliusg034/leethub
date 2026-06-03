use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        // this is a two pointer problem
        // let's try brute force solution first
        // for the second try lets use the hashmap

        let mut indexes = HashMap::new();

        for (i, &num) in nums.iter().enumerate() {
            let compliment = target - num;

            if let Some(&j) = indexes.get(&compliment) {
                return vec![j as i32, i as i32];
            }

            indexes.insert(num, i);
        }

        vec![]
    }
}