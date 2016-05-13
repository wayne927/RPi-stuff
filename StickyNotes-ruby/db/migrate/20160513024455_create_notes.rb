class CreateNotes < ActiveRecord::Migration
  def change
    change_table :notes do |t|
      t.string :title
      t.text :content
      t.string :color
      t.timestamps
    end
  end
end
