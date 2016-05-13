class FixContentTypo < ActiveRecord::Migration
  def change
    rename_column :notes, :conent, :content
  end
end
