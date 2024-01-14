use std::vec;

pub fn run() {
    let s: i32 = Solution::climb_stairs(3);
    println!("{s}");
}
struct Solution;
impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if (n == 0) {
            return 1;
        }
        if (n == 1) {
            return 1;
        }
        let (mut f, mut s, mut ans): (i32, i32, i32) = (1, 1, 0);
        for i in 2..=n {
            ans = f + s;
            s = f;
            f = ans;
        }
        return ans;
    }
}
