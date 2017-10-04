#!/bin/bash
fn(){
  #alph=({a..z} {A..Z} {0..9})
  a=({a..z})
  b=({A..Z})
  c=$a[*]$b[*]
  #for i in ${alph[*]}
  for i in ${c[*]}
  do
    echo -n $i
  done
  echo
}

fn
