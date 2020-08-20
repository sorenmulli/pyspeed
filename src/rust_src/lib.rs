#![crate_type = "dylib"]

#[no_mangle]
pub extern fn rootloop(N: isize) -> f64 {
    let mut s = 0.;
    println!("0");
    for n in (0..N).step_by(2) {
        s += (n as f64).sqrt();
    }
    return s;
}

