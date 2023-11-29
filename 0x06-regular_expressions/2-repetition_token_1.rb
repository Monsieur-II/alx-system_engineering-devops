#!/usr/bin/env ruby

if ARGV[0].nil?
  puts "Please provide an argument"
else
  puts ARGV[0].scan(/hb?tn/).join
end
