class CreateHahas < ActiveRecord::Migration
  def change
    create_table :hahas do |t|

      t.timestamps
    end
  end
end
