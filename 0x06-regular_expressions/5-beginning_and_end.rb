#!/usr/bin/env ruby

if ARGV[0].nil?
  puts "Please provide an argument"
else
  puts ARGV[0].scan(/h.n/).join
end
