use std::vec;

pub fn run() {
    for i in 0..20 {
        let s: bool = Solution::is_happy(i);
        println!("{s}");
    }
}

pub struct Solution;
impl Solution {
    fn get_sum(mut n: i32) -> i32 {
        let mut sum: i32 = 0;
        let (mut rem, quo): (i32, i32);
        while (n > 0) {
            rem = n % 10;
            n = n / 10;
            sum += rem * rem;
        }
        sum
    }
    pub fn is_happy(n: i32) -> bool {
        let mut sum_all: Vec<i32> = vec![];
        let mut s: i32 = n;
        let (mut status, mut loop_status): (bool, bool) = (true, true);
        'outer_while: loop {
            s = Solution::get_sum(s);
            if s == 1 {
                break;
            }
            for v in sum_all.iter() {
                if v.to_owned() == s {
                    loop_status = false;
                    status = false;
                    break;
                }
            }
            if !loop_status {
                break;
            }
            sum_all.push(s);
        }
        return status;
    }
}
