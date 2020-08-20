
#[no_mangle]
#[allow(non_snake_case)]
fn rootloop(N: isize) -> f64 {
    let mut s = 0.;
    for n in (0..N).step_by(2) {
        s += (n as f64).sqrt();
    }
    return s;
}

