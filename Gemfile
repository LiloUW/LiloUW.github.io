source "https://rubygems.org"

# Matches the Jekyll version and plugins used by GitHub Pages.
gem "github-pages", group: :jekyll_plugins
gem "webrick" # required by `jekyll serve` on Ruby 3+

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]
