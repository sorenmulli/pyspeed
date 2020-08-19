use std::time;

fn main() {
    let reps = 10;
    let mut total_time = 0.;
    for _rep in 0..reps {
        let start = time::Instant::now();
        get_sum(1e8 as isize);
        let elapsed = start.elapsed().as_nanos() as f64;
        total_time += elapsed;
        println!("{} ns", elapsed)
    }
    total_time /= reps as f64;
    println!("{} s", total_time / 1e9);
}

fn get_sum(N: isize) -> f64 {
    let mut s = 0.;
    for n in (0..N).step_by(2) {
        s += (n as f64).sqrt();
    }
    return s;
}
