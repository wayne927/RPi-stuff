class NotesController < ApplicationController

    def home
        @notes = Note.all
    end

    def new
        @note = Note.new
    end

    def create
        @note = Note.new(note_params)
        if @note.save
            redirect_to '/notes'
        else
            render 'new'
        end

    end


    private
    def note_params
        params.require(:note).permit(:content, :title, :color)
    end

end
