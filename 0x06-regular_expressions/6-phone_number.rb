#!/usr/bin/env ruby

if ARGV[0].nil?
  puts "Please provide an argument"
else
  puts ARGV[0].scan(/^\d{10,10}/).join
end
