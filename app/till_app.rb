require 'sinatra/base'
require '.app/lib/till'

class TillApp < Sinatra::Base

  set :views, Proc.new { File.join(root, "views") }
  set :public_folder, Proc.new { File.join(root, "public") }

  till = Till.new

  get '/' do
    'hello world'
  end



  # start the server if ruby file executed directly
  run! if app_file == $0
end