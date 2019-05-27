require "csv"
require "pry"
require "rb-readline"

File.open("script.rpy", "w") do |script|
  CSV.foreach("data/otis.csv") do |row|
    if row[0]
      script << "label #{row[0]}\n\n"
    end

    script << "\s\s\s\s#{row[1]}\n\n"
  end
end
